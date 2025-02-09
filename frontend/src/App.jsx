import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import './App.css';
// import Home from './components/Home';
// import Login from './components/Login';
// import Signup from './components/Signup';
// import Landpage from './components/Landpage';
// import PasswordResetRequest from './components/PasswordResetRequest';
// import ProtectedRoute from './components/ProtectedRoutes';
// import PasswordReset from './components/PasswordReset';
// import Message from './message';
// import Index from './views/core';
import MainWrapper from "../src/layouts/MainWrapper"



import Index from "./views/core/Index";
import Detail from "./views/core/Detail";
import Search from "./views/core/Search";
import Category from "./views/core/Category";
// import About from "./views/pages/About";
// import Contact from "./views/pages/Contact";
import Register from "./views/auth/Register";
import Login from "./views/auth/Login";
import Logout from "./views/auth/Logout";
import ForgotPassword from "./views/auth/ForgotPassword";
import CreatePassword from "./views/auth/CreatePassword";
import Dashboard from "./views/dashboard/Dashboard";
import Posts from "./views/dashboard/Posts";
import AddPost from "./views/dashboard/AddPost";
import EditPost from "./views/dashboard/EditPost";
import Comments from "./views/dashboard/Comments";
// import Notifications from "./views/dashboard/Notifications";
import Eventbooking from "./views/dashboard/Eventbooking";
import Profile from "./views/dashboard/Profile";



function App() {
  const location = useLocation()
  const noNavbar = location.pathname === "/signup" || location.pathname === "/" || location.pathname.includes("password")

  return (
      <div className="App">
          <Routes>
          <Route path="/" element={<MainWrapper><Index /></MainWrapper>} />
          <Route path="/:slug/" element={<MainWrapper><Detail /></MainWrapper>} />
          <Route path="/category/:slug/" element={<MainWrapper><Category /></MainWrapper>} />
          <Route path="/search/" element={<MainWrapper><Search /></MainWrapper>} />

          {/* Authentication */}
          <Route path="/register/" element={<MainWrapper><Register /></MainWrapper>} />
          <Route path="/login/" element={<MainWrapper><Login /></MainWrapper>} />
          <Route path="/logout/" element={<MainWrapper><Logout /></MainWrapper>} />
          <Route path="/forgot-password/" element={<MainWrapper><ForgotPassword /></MainWrapper>} />
          <Route path="/create-password/" element={<MainWrapper><CreatePassword /></MainWrapper>} />

          {/* Dashboard */}
          <Route path="/dashboard/" element={<MainWrapper><Dashboard /></MainWrapper>} />
          <Route path="/posts/" element={<MainWrapper><Posts /></MainWrapper>} />
          <Route path="/add-post/" element={<MainWrapper><AddPost /></MainWrapper>} />
          <Route path="/edit-post/" element={<MainWrapper><EditPost /></MainWrapper>} />
          <Route path="/comments/" element={<MainWrapper><Comments /></MainWrapper>} />
          {/* <Route path="/notifications/" element={<MainWrapper><Notifications /></MainWrapper>} /> */}
          <Route path="/eventbooking/" element={<MainWrapper><Eventbooking /></MainWrapper>} />
          <Route path="/profile/" element={<MainWrapper><Profile /></MainWrapper>} />

          {/* Pages
          <Route path="/about/" element={<MainWrapper><About /></MainWrapper>} />
          <Route path="/contact/" element={<MainWrapper><Contact /></MainWrapper>} /> */}

        





          {/* <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/message" element={<Message />} />
          <Route path="/request/password_reset" element={<PasswordResetRequest/>} />
          <Route path="/password-reset/:token" element={<PasswordReset/>} />
          <Route element={<ProtectedRoute/>}>
            <Route path='/home' element={<Home />}></Route>
          </Route> */}
          {/* <Route path="/home" element={<ProtectedRoute element={<Home />} />} /> */}
          {/* <Route path="/home" element={<Home />} /> */}
          
          
        </Routes>
      </div>

      
  );
}

export default App;