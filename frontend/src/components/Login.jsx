import React from 'react';
import { Link } from 'react-router-dom';
import '../Login.css';
import email_icon from '../assets/email.png';
import password_icon from '../assets/password.png';
import MytextField from './forms/MytextField';
import MypassField from './forms/MypassField';
import MyButton from './forms/MyButton';
import { useForm } from 'react-hook-form';
import AxiosInstance from './Axiosinstance';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate();
  const { handleSubmit, control } = useForm();

  const submission = (data) => {
    AxiosInstance.post(`login/`, {
      username: data.username,
      email: data.email,
      password: data.password,
    })
      .then((response) => {
        console.log(response);
        localStorage.setItem('Token', response.data.token);
        navigate(`/home`);
      })
      .catch((error) => {
        console.error('Error during login', error);
      });
  };

  return (
    <div className="background"> {/* Apply background */}
      <div className="container">
        <form onSubmit={handleSubmit(submission)}>
          <div className="header">
            <div className="text">Login</div>
            <div className="underline"></div>
          </div>
          <div className="inputs">
            <div className="input">
              <img src={email_icon} alt="Email Icon" />
              <MytextField label="Email" name="email" control={control} />
            </div>
            <div className="input">
              <img src={password_icon} alt="Password Icon" />
              <MypassField label="Password" name="password" control={control} />
            </div>
          </div>
          <div className="forgot-password">
            <Link to="/request/password_reset">Forgot password? Click here</Link>
          </div>
          <div className="submit-container">
            <MyButton type="submit" label={"Login"} />
            <div className="switch">
              Don't have an account? <Link to="/signup">Sign Up</Link>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
