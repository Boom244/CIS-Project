connSocket = new WebSocket("ws://10.84.3.157:5446")

document.getElementById("pingbutton").addEventListener("click", (event) => {
  connSocket.send(toString(Date.now()));
});

connSocket.onmessage = function(event) {
  console.log(event.data);
};