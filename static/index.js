var state = {}

$(document).ready(function() {
  console.log('wewt');
  landing();
})

$(document).on('click', '.square', function(e) {
  console.log(e.target.id);

})

function revealSquare(x, y) {
  $.ajax({
    url: '/reveal_square',
    type: 'post',
    data: { x, y },
    success: function(res) {
      console.log(res);
    }

  })
}

function landing() {
  const root = document.getElementById('root');
  const button = document.createElement('button');
  button.innerText = 'START!'
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
    const square = document.createElement('div');
    square.className = 'square'
    square.id = `${x} ${y}`
    if (state.board[x][y].bomb === true) {
      square.innerText = 'B';
    }
    row.appendChild(square);
  }
  return row;
}

function drawSquare() {

}