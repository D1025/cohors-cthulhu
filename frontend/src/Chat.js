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
  componentDidUpdate(prevProps) {
    // Check if props.nickname has changed and update the state accordingly
    if (this.props.nickname !== prevProps.nickname) {
      this.setState({ nickname: this.props.nickname });
    }
  }
  sendMessage() {
    this.forceUpdate();
    const message = {
      type: "message",
      nickname: this.state.nickname, // Use this.state.nickname
      index: this.state.messages.length,
      message: this.state.input,
    };
    this.props.ws.send(JSON.stringify(message));
    this.setState({ input: "" });
    return false;
  }
  handleInputChange = (event) => {
    this.setState({ input: event.target.value });
  };
  handleEnterPress = (e) =>{
    if(e.key === 'Enter'){
      this.sendMessage()
    }
  }
  render() {
    const { messages } = this.props;
    messages.map((messsage, index) => {
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
                message.nickname === this.props.nickname ? (
                <div className={"author-message"}>
                  <li key={i.index}>
                  {message.nickname}: {message.message}
                  </li>
                  <div className={"chat-spacer"}></div>
                </div>
                ) :
                    (
                        <div className={"someone-message"}>
                          <li key={i.index}>
                            {message.nickname}: {message.message}
                          </li>
                          <div className={"chat-spacer"}></div>
                        </div>
                    )
            )
          )}
        </ul>
        <div id="input-box">
          <input
            type="text"
            placeholder="Enter message..."
            value={this.state.input}
            onChange={this.handleInputChange}
            onKeyDown={this.handleEnterPress}
          ></input>
          <button  onClick={this.sendMessage}>Send</button>
        </div>
      </div>
    );
  }
}
