import React from "react";
import "./Chat.css";

export default class Chat extends React.Component {
  constructor(props) {
    super(props);
    this.sendMessage = this.sendMessage.bind(this);
    this.state = {
      messages: props.messages,
    };
  }
  sendMessage() {
    const message = { 1: "test" };
    console.log(this.props.ws);
    this.props.ws.send(JSON.stringify(message));
  }

  render() {
    const { messages } = this.props;
    messages.map((messsage, index) => {
      console.log(messsage);
    });
    return (
      <div className="chat-box">
        <h1 id="chat-name">CHAT</h1>
        <ul>
          {messages.map((message, index) => (
            <li key={index}>{message[index]}</li>
          ))}
        </ul>
        <div>
          <button onClick={this.sendMessage}>Wyślij wiadomość</button>
        </div>
      </div>
    );
  }
}
