var MASTER = {}

$(document).ready(function() {
  console.log('wewt');
  landing();
})

function landing() {
  let root = document.getElementById('root');
  let button = document.createElement('button');
  button.innerText = 'START!'
  button.addEventListener('click', function() {
    $.ajax({
      url: '/start',
      success: function(res) {
        console.log(res) 
      }
    })
  })
  root.appendChild(button);
}