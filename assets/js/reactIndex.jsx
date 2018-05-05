import React from 'react';
import ReactDOM from 'react-dom';
import UserInterface from './react/UserInterface/UserInterface.jsx';

export default function startReact() {
  const reactRoot = document.getElementById('react-root');
  ReactDOM.render(
    <UserInterface />,
    reactRoot,
  );
}
