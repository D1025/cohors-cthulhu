import React from "react";
import "./Chat.css";

export default class Chat extends React.Component {
  constructor(props) {
    super(props);
    this.sendMessage = this.sendMessage.bind(this);
    this.state = {
      ws: null,
      messages: [],
    };
  }
  sendMessage() {
    const { ws } = this.state;
    const message = { text: "test" };
    ws.send(JSON.stringify(message));
  }

  componentDidMount() {
    const ws = new WebSocket("ws://localhost:8080");

    ws.addEventListener("open", () => {
      console.log("WebSocket connection opened");
      this.state.messages.push("Connected");
      this.setState({ messages: this.state.messages });
    });

    ws.addEventListener("message", (event) => {
      console.log("siusiak");
      // Handle incoming messages
      const newMessage = JSON.parse(event.data);

      // Update state to add the new message
      this.setState((prevState) => ({
        messages: [...prevState.messages, newMessage],
      }));
    });

    ws.addEventListener("close", () => {
      console.log("WebSocket connection closed");

      // You can implement reconnection logic here if needed
    });

    // Save the WebSocket instance in the component's state
    this.setState({ ws });
  }

  componentWillUnmount() {
    // Close the WebSocket connection when the component unmounts
    if (this.state.ws) {
      this.state.ws.close();
    }
  }

  render() {
    const { messages } = this.state;
    return (
      <div className="chat-box">
        <h1 id="chat-name">CHAT</h1>
        <ul>
          {messages.map((message, index) => (
            <li key={index}>{message}</li>
          ))}
        </ul>
        <div>
          <button onClick={this.sendMessage}>Wyślij wiadomość</button>
        </div>
      </div>
    );
  }
}
