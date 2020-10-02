/** Checking the game winner. */

//>
function checkWinner() {
  if (gameOver) {
    $scoreMessage.html("Yay!");
    score += 100;
  }
}
//<

// more code follows ...