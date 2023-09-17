import { Component, useEffect, useState } from "react";
import Chat from "./Chat";
import Sheet from "./Sheet";
import "./Wrapper.css";

class Wrapper extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ws: null,
      messages: [],
      isWebSocketOpen: false,
      isNicknameSet: false,
      inputNick: "",
      nick: "",
    };
  }
  componentDidMount() {
    const ws = new WebSocket("ws://localhost:8080");

    ws.addEventListener("open", () => {

      const newMessage = {
        index: 0,
        message: "Connection established",
      };
      this.setState({ isWebSocketOpen: true });
      this.setState((prevState) => ({
        messages: [...prevState.messages, newMessage],
      }));
    });
    ws.addEventListener("message", (event) => {
      // Handle incoming messages

      const newMessage = JSON.parse(event.data);


      // Update state to add the new message
      if (newMessage.type === "message") {
        this.setState((prevState) => ({
          messages: [...prevState.messages, newMessage],
        }));
      }
    });

    ws.addEventListener("close", () => {
      console.log("WebSocket connection closed");

      // You can implement reconnection logic here if needed
    });

    // Save the WebSocket instance in the component's state

    this.setState({ ws });
  }
  componentDidUpdate(prevState) {}

  componentWillUnmount() {
    // Close the WebSocket connection when the component unmounts
    if (this.state.ws) {
      this.state.ws.close();
    }
  }
  waitForWebSocketConnection() {
    setTimeout(() => {
      if (this.state.ws.readyState === 1) {
        console.log("test");
        console.log(this.state.ws);
        return true;
      } else {
        this.waitForWebSocketConnection();
      }
    }, 1);
  }
  setNickname = () => {
    this.setState({ nick: this.state.inputNick });
    this.setState({ isNicknameSet: true });
  };

  handleNickInput = (event) => {
    this.setState({ inputNick: event.target.value });
  };
  handleEnterPress = (e) =>{
    if(e.key === 'Enter'){
      this.setNickname()
    }
  }
  render() {
    return (
      <div>
        {!this.state.isNicknameSet ? (
          <div className="above nicknameset">
            <input type="text" onChange={this.handleNickInput} onKeyDown={this.handleEnterPress}></input>
            <button onClick={this.setNickname}>Login</button>
          </div>
        ) : this.state.isWebSocketOpen ? (
          <div className="container box">
            <Sheet
                ws={this.state.ws}
                nickname={this.state.nick}
            />
            <Chat
              ws={this.state.ws}
              messages={this.state.messages}
              nickname={this.state.nick} // Pass nick as the nickname prop
            />
          </div>
        ) : (
          <p>Connecting to WebSocket...</p>
        )}
      </div>
    );
  }
}

export default Wrapper;
