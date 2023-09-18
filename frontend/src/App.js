import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.websocket = new WebSocket('ws://104.248.37.81:8080');

    this.websocket.onopen = () => {
      console.log('Połączono z serwerem WebSocket.');
    };

    this.websocket.onmessage = (event) => {
      console.log('Odebrano dane: ' + event.data);
    };
  }

  sendMessage = () => {
    this.websocket.send('To jest wiadomość od klienta.');
  }

  render() {
    return (
      <div>
        <button onClick={this.sendMessage}>Wyślij wiadomość</button>
      </div>
    );
  }
}

export default App;