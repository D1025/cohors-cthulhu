import { Component, useEffect, useState } from "react";
import Chat from "./Chat";
import Sheet from "./Sheet";
import "./Wrapper.css";

export default class Wrapper extends Component {
  constructor(props) {
    super(props);
    this.handleNickInput = this.handleNickInput.bind(this);
    this.setNickname = this.setNickname.bind(this);
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
      console.log("Connection established");
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
      console.log(event.data);
      const newMessage = JSON.parse(event.data);
      console.log(newMessage);

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
  setNickname() {
    this.setState({ nick: this.state.input });
    this.setState({ isNicknameSet: true });
  }
  handleNickInput() {
    this.setState({ input: this.state.input });
  }
  render() {
    return (
      <div>
        {this.state.isNicknameSet != true ? (
          <div className="above nicknameset">
            <input type="text" onChange={this.handleNickInput}></input>
            <button onClick={this.setNickname}>Login</button>
          </div>
        ) : this.state.isWebSocketOpen ? (
          // Render the component when WebSocket is open
          <div className="container box">
            <Sheet ws={this.state.ws} />
            <Chat
              ws={this.state.ws}
              messages={this.state.messages}
              nickname={this.state.inputNick}
            />
          </div>
        ) : (
          // Render something else or a loading indicator
          <p>Connecting to WebSocket...</p>
        )}
      </div>
    );
  }
}
