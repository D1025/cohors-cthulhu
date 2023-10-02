import { Component} from "react";


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
  wsUrl = process.env.REACT_APP_PROD === 'true' ? 'ws://localhost:8080' : 'ws://104.248.37.81:8081';
  componentDidMount() {
    const searchParams = new URLSearchParams(window.location.search);
    const nickname = searchParams.get("nickname");
    if (nickname) {
      this.setState({ nick: nickname, isNicknameSet: true });
    }
    const ws = new WebSocket(this.wsUrl);

    ws.addEventListener("open", () => {
      console.log(`ws connected on ${this.wsUrl}`)
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
      if(newMessage.type  === "damage"){
        let messageContent = `dmg: ${newMessage.damage} effects: ${newMessage.effects} ` + `<${newMessage.rolls.join("> <")}>`
        let damageMessage = {
          nickname: newMessage.nickname,
          message: messageContent,
        }
        this.setState((prevState) => ({
          messages: [...prevState.messages, damageMessage],
        }));
      }
      if(newMessage.type === "roll"){
        let focusChecked = ''
        if (newMessage.focus){
          focusChecked = '[F] '
        }
        let messageContent = `${focusChecked}${newMessage.attribute} + ${newMessage.skill}= ` + `<${newMessage.rolls.join("> <")}>` + `success:${newMessage.successes} ` + `complication:${newMessage.complication}`;
        let rollMessage = {
          nickname: newMessage.nickname,
          message: messageContent,
        }
        this.setState((prevState) => ({
          messages: [...prevState.messages, rollMessage],
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
    window.location.href = '?nickname=' + this.state.inputNick;
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
