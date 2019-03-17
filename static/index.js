var state = {}

$(document).ready(function() {
  console.log('wewt');
  landing();
})

$(document).on('click', '.square', function(e) {
  const target = e.target;
  const id = target.id;
  revealSquare(target, id);

})

function revealSquare(target, id) {
  const coord = id.split(' ');
  const x = coord[0];
  const y = coord[1];
  if (state.board[x][y].bomb === true) {
    console.log('BOOOOOOM');
    target.className = 'bomb';
  }
}

function landing() {
  const root = document.getElementById('root');
  const button = document.createElement('button');
  button.innerText = 'Create New Game';
  button.id = 'start';
  button.addEventListener('click', generateNewGame);
  root.appendChild(button);
}

function generateNewGame() {
    $.ajax({
      url: '/start',
      success: function(res) {
        state = JSON.parse(res);
        drawBoard();
      }
    })
}

function drawBoard() {
  const root = document.getElementById('root');
  const board = document.createElement('div');
  board.className = 'board';
  root.appendChild(board);
  for (let y = 0; y < state.size; y++) {
    const row = drawRow(y);
    board.appendChild(row);
  } 
}

function drawRow(y) {
  const row = document.createElement('div');
  row.className = 'row';
  for (let x = 0; x < state.size; x++) {
    const square = drawSquare(x, y);
    row.appendChild(square);
  }
  return row;
}

function drawSquare(x, y) {
    const square = document.createElement('div');
    square.className = 'square'
    square.id = `${x} ${y}`
    const loc = state.board[x][y];
    if (loc.bomb === true) {
      square.innerText = 'B';
    } else {
      square.innerText = loc.warning;
    }
    return square;
}