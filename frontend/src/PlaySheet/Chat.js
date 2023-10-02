import React from "react";
import "./Chat.css";

export default class Chat extends React.Component {
  constructor(props) {
    super(props);
    this.chatContainerRef = React.createRef();
    this.sendMessage = this.sendMessage.bind(this);
    this.state = {
      messages: props.messages,
      input: "",
      nickname: props.nickname || "",
    };
  }
  componentDidUpdate(prevProps) {
    
    if (this.props.nickname !== prevProps.nickname) {
      this.setState({ nickname: this.props.nickname });
    }

    // Check if new messages have been added and scroll to the bottom
    if (this.props.messages.length !== prevProps.messages.length) {
      this.scrollToBottom();
    }
  }
  componentDidMount() {
    const apiURL = process.env.REACT_APP_PROD === 'true'
? "http://localhost:8087"
: "http://104.248.37.81:8087";
// fetch(apiURL + `/chat`)
// .then((response) => {
//   if (!response.ok) {
//     throw new Error("Network response was not ok");
//   }
//   console.log(response)
//   return response.json();
// })
// .then((data) => {
//   this.setState({
//     messages: data
//   });
// })
// .catch((error) => {
//   console.error("API Error:", error); // Log any error
//   this.setState({
//     error: error,
//     isLoading: false,
//   });
// });

    // Call scrollToBottom when the component first mounts to ensure initial scrolling
    this.scrollToBottom();
  }
  handleReloadComponent = () => {
    // Construct the URL with the nickname parameter
    const url = `/?nickname=${encodeURIComponent(this.props.nickname)}`;

    // Reload the page with the updated URL
    window.location.href = url;
}
  scrollToBottom() {
    if (this.chatContainerRef.current) {
      const chatContainer = this.chatContainerRef.current;
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  }
  sendMessage() {
    this.forceUpdate();
    const message = {
      type: "message",
      nickname: this.state.nickname, 
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
        <ul className="chat" ref={this.chatContainerRef}>
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
