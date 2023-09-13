import { Component, useEffect, useState } from "react";
import Chat from "./Chat";
import Sheet from "./Sheet";

export default class Wrapper extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ws: null,
      messages: [],
      isWebSocketOpen: false,
    };
  }
  componentDidMount() {
    const ws = new WebSocket("ws://localhost:8080");

    ws.addEventListener("open", () => {
      console.log("Connection established");
      this.state.messages.push({ 0: "Connection established" });
      this.setState({ isWebSocketOpen: true });
    });
    ws.addEventListener("message", (event) => {
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
  render() {
    return (
      <div>
        {this.state.isWebSocketOpen ? (
          // Render the component when WebSocket is open
          <div className="container box">
            <Sheet ws={this.state.ws} />
            <Chat ws={this.state.ws} messages={this.state.messages} />
          </div>
        ) : (
          // Render something else or a loading indicator
          <p>Connecting to WebSocket...</p>
        )}
      </div>
    );
  }
}
