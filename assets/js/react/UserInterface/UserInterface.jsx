import React from 'react';
// import jQuery from 'jquery';
// import PropTypes from 'prop-types';


class UserInterface extends React.PureComponent {
  constructor(props) {
    super(props);
    console.log('UserInterface.props ---> ', props);

    const WebSocket = window.WebSocket || window.MozWebSocket;
    const url = `ws://${window.location.host}/ws/index/`;
    this.voteSocket = new WebSocket(url);
    this.voteSocket.onmessage = (e) => {
      // const data = JSON.parse(e.data);
      console.log(`SERVER: ${e.data}`);
    };

    this.exampleClick = this.exampleClick.bind(this);
  }

  componentDidMount() {}

  exampleClick() {
    console.log(this, this.props);
    this.voteSocket.send(JSON.stringify({
      message: 'this is my message from browser',
    }));
  }

  render() {
    return (
      <div>
        Hello react! <br />
        <button onClick={this.exampleClick}>Example Button</button>
      </div>
    );
  }
}

UserInterface.defaultProps = {};

UserInterface.propTypes = {};

export default UserInterface;
