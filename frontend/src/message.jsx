import React, { useState, useEffect } from 'react';
import './message.css';
import Pusher from "pusher-js";

const Message = () => {
  const [username, setUsername] = useState('username');
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    Pusher.logToConsole = true;

    const pusher = new Pusher('e0e5d4648c9e1528a190', {
      cluster: 'ap2'
    });

    const channel = pusher.subscribe('chat');
    channel.bind('message', function (data) {
      setMessages((prevMessages) => [...prevMessages, data]);
    });

    return () => {
      channel.unbind_all();
      channel.unsubscribe();
    };
  }, []);

  const submit = async (e) => {
    e.preventDefault();

    if (message.trim()) {
      try {
        await fetch('http://localhost:8000/api/messages', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, message })
        });

        setMessage('');
      } catch (error) {
        console.error('Error submitting message:', error);
      }
    }
  };

  return (
    <div className="container">
      <div className="d-flex flex-column align-items-stretch flex-shrink-0 bg-body-tertiary">
        <div className="d-flex align-items-center flex-shrink-0 p-3 link-body-emphasis text-decoration-none border-bottom">
          <input
            placeholder="Username"
            className="fs-5 fw-semibold"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="list-group list-group-flush border-bottom scrollarea">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message-container ${msg.username === username ? 'sent' : ''}`}
            >
              <div className="message-bubble">
                <div className="message-username">{msg.username}</div>
                <div className="message-text">{msg.message}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
      <form onSubmit={submit}>
        <input
          className="form-control"
          placeholder="Write a message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
    </div>
  );
};

export default Message;
