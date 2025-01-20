import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import './App.css';
import Home from './components/Home';
import Login from './components/Login';
import Signup from './components/Signup';
import Landpage from './components/Landpage';
import PasswordResetRequest from './components/PasswordResetRequest';
import ProtectedRoute from './components/ProtectedRoutes';
import PasswordReset from './components/PasswordReset';
import Message from './message';




function App() {
  const location = useLocation()
  const noNavbar = location.pathname === "/signup" || location.pathname === "/" || location.pathname.includes("password")

  return (
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/message" element={<Message />} />
          <Route path="/request/password_reset" element={<PasswordResetRequest/>} />
          <Route path="/password-reset/:token" element={<PasswordReset/>} />
          <Route element={<ProtectedRoute/>}>
            <Route path='/home' element={<Home />}></Route>
          </Route>
          {/* <Route path="/home" element={<ProtectedRoute element={<Home />} />} /> */}
          {/* <Route path="/home" element={<Home />} /> */}
          
          
        </Routes>
      </div>

      
  );
}

export default App;