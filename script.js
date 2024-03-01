connSocket = new WebSocket("ws://10.84.3.157:5446")

connSocket.addEventListener("open", (event) => {
    connSocket.send("Hello Server!");
  });