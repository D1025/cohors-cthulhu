import React from "react";
import "./Chat.css";

export default class Chat extends React.Component {
  constructor(props) {
    super(props);
    this.sendMessage = this.sendMessage.bind(this);
    this.state = {
      messages: props.messages,
      input: "",
      nickname: props.nickname || "",
    };
  }
  sendMessage() {
    const message = {
      type: "message",
      nickname: this.props.nickname,
      index: this.state.messages.length,
      message: this.state.input,
    };
    console.log(this.props.ws);
    this.props.ws.send(JSON.stringify(message));
    this.setState({ input: "" });
  }
  handleInputChange = (event) => {
    this.setState({ input: event.target.value });
  };
  render() {
    const { messages } = this.props;
    messages.map((messsage, index) => {
      console.log(messsage);
    });
    return (
      <div className="chat-box">
        <h1 id="chat-name">CHAT</h1>
        <div className="break"></div>
        <ul className="chat">
          {messages.map((message, i) =>
            i == 0 ? (
              <h3>{message.message}</h3>
            ) : (
              <li key={i.index}>
                {message.nickname}:{message.message}
              </li>
            )
          )}
        </ul>
        <div id="input-box">
          <input
            type="text"
            placeholder="Enter message..."
            value={this.state.input}
            onChange={this.handleInputChange}
          ></input>
          <button onClick={this.sendMessage}>Wyślij wiadomość</button>
        </div>
      </div>
    );
  }
}
