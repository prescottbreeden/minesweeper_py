var state = {}

$(document).ready(function() {
  landing();
})

$(document).on('click', '.square', function(e) {
  const target = e.target;
  const id = target.id;
  revealSquare(target, id);
})

function landing() {
  const root = document.getElementById('root');
  const button = makeButton('Create New Game');
  root.appendChild(button);
}

function makeButton(text) {
  const button = document.createElement('button');
  button.innerText = text;
  button.id = 'start';
  button.addEventListener('click', generateNewGame);
  return button; 
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
  root.innerHTML = '';
  const button = makeButton('Reset');
  root.appendChild(button);
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
    square.className = 'square';
    square.id = `${x} ${y}`;
    return square;
}

function revealSquare(target, id) {
  target.classList.remove('square');
  target.classList.add('reveal');
  const loc = getLocation(id);
  if (loc.bomb === true) {
    console.log('boooooom');
    target.classList.add('bomb');
    target.classList.add('explode');
  } 
  else if (loc.warning === 0) {
    floodFill(target, id);
  }
  else if (loc.warning > 0) {
    addWarning(target, loc.warning);
  }
}

function addWarning(target, num) {
    switch (num) {
      case 1:
        target.classList.add('blue-text');
        break;
      case 2:
        target.classList.add('green-text');
        break;
      case 3:
        target.classList.add('red-text');
        break;
      case 4:
        target.classList.add('purple-text');
        break;
      case 5:
        target.classList.add('brown-text');
        break;
      case 6:
        target.classList.add('cyan-text');
        break;
    }
    target.innerText = num;
}

function floodFill(ele, id) {
  if (!ele) return;
  ele.classList.remove('square');
  ele.classList.add('reveal');
  const loc = getLocation(id);
  if (loc.warning !== 0) {
    addWarning(ele, id);
  }
}

function getLocation(id) {
  const coord = id.split(' ');
  const x = coord[0];
  const y = coord[1];
  return state.board[x][y];
}
