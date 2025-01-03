import React from 'react';
import { Link } from 'react-router-dom';
import '../Login.css';
import user_icon from '../assets/person.png';
import email_icon from '../assets/email.png';
import password_icon from '../assets/password.png';
import MytextField from './forms/MytextField';
import MypassField from './forms/MypassField';
import MyButton from './forms/MyButton';
import { useForm } from 'react-hook-form';
import AxiosInstance from './Axiosinstance';
import { useNavigate } from 'react-router-dom';
import {yupResolver} from "@hookform/resolvers/yup"
import * as yup from "yup"

const Signup = () => {
  const navigate = useNavigate();
 
  
  const schema = yup
  .object({
    email:yup.string().email('Field expects an email address').required('Email is a required field'),
    password: yup.string()
                .required('Password is required field')
                .min(8, 'Password must be at least 8 characters')
                .matches(/[A-Z]/,'Password must contain at least one uppercase letter')
                .matches(/[a-z]/,'Password must contain at least one lowercase letter')
                .matches(/[0-9]/,'Password must contain at least one number')
    password2: yup.string().required('password confirmation is a required field')
                  .oneOf([yup.ref('password'),null], 'Passowrds must match')
  }) 

  const { handleSubmit, control, watch } = useForm({resolver:yupResolver(schema)})

    const submission = (data) => {
      AxiosInstance.post(`register/`,{
        username: data.username,
        email:data.email,
        password:data.password,
      })
       
      .then(() => {
        navigate(`/`)
      }
    )
  }

  return (
    <div className="container">
      <form onSubmit={handleSubmit(submission)}>
        <div className="header">
          <div className="text">Sign Up</div>
          <div className="underline"></div>
        </div>
        <div className="inputs">
          <div className="input">
            <img src={user_icon} alt="User Icon" />
            <MytextField label="Username" name="username" control={control} />
          </div>
          <div className="input">
            <img src={email_icon} alt="Email Icon" />
            <MytextField label="Email" name="email" control={control} />
          </div>
          <div className="input">
            <img src={password_icon} alt="Password Icon" />
            <MypassField label="Password" name="password" control={control} />
          </div>
          <div className="input">
            <img src={password_icon} alt="Confirm Password Icon" />
            <MypassField label="Confirm Password" name="password2" control={control} />
          </div>
        </div>
        <div className="submit-container">
          <MyButton type="submit" label="Sign Up" />
          <div className="switch">
            Already have an account? <Link to="/">Login</Link>
          </div>
        </div>
      </form>
    </div>
  );
};


export default Signup;
