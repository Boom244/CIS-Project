connSocket = new WebSocket("ws://10.84.3.157:5446")

document.getElementById("pingbutton").addEventListener("click", (event) => {
  connSocket.send(Date.now());
});

connSocket.onmessage = function(event) {
  console.log(event.data);
};

document.addEventListener("keydown",function(event){
  connSocket.send("ACTION:"+event.key)
});