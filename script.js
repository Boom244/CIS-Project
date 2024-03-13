connSocket = new WebSocket("ws://10.84.3.157:5446")
lastSendval = null
document.getElementById("pingbutton").addEventListener("click", (event) => {
  connSocket.send(Date.now());
});

connSocket.onmessage = function(event) {
  console.log(event.data);
};

document.addEventListener("keydown",function(event){
  sendval = null;
  switch(event.key)
  {
    case "w":
      sendval = "FORWARD";
      break;
    case "s":
      sendval = "BACKWARD";
      break;
    case "a":
      sendval = "LEFT";
      break;
    case "d":
      sendval = "RIGHT";
      break;
  }
  if (sendval != lastSendval)
  {
    connSocket.send(sendval)
    lastSendval = sendval
    console.log(sendval)
  }
});

document.addEventListener("keyup",function(event){
  connSocket.send("STOP");
  console.log("STOP")
  lastSendval = "STOP"
});

