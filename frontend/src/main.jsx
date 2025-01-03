import { StrictMode } from 'react';
import ReactDOM from 'react-dom/client'; // Import ReactDOM correctly
import App from './App.jsx';
import { BrowserRouter as Router } from 'react-router-dom';

// Create a root element and render your app
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <StrictMode>
    <Router>
      <App/>
    </Router>
  </StrictMode>
);
