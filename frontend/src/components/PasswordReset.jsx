import React, { useEffect, useState } from 'react'; // Consolidated React import
import {useParams} from 'react-router-dom';
import '../Login.css';
import MyButton from './forms/MyButton';
import { useForm } from 'react-hook-form';
import AxiosInstance from './Axiosinstance';
import { useNavigate } from 'react-router-dom';
import MyMessage from './Message';

const PasswordReset = () => {
    const navigate = useNavigate();
    const { handleSubmit, control } = useForm();
    const [showMessage, setShowMessage] = useState(false); // Fixed `useState`
    const {token} = useParams()
    console.log(token)

    const submission = (data) => {
        AxiosInstance.post(`api/password_reset/confirm/`, {
            password: data.password,
            token:token,
            username: data.username,
            email: data.email,
        })
        .then((response) => {
            setShowMessage(true);
            setTimeout(() =>{
            navigate ('/')
        },2000)
        })
        .catch((error) => {
            console.error('Error during password reset request', error);
        });
    };

    return (
        <div className="container">
             {showMessage && (
                    <MyMessage text="Your passowrd reset was successfull, You wll be directed to the login page in a second " />
                )}
            <form onSubmit={handleSubmit(submission)}>
               
                <div className="header">
                    <div className="text">Reset password</div>
                </div>
                <div className="inputs">
                    <div className="input">
                              <img src={password_icon} alt="Password Icon" />
                              <MypassField label="Password" name="password" control={control} />
                    </div>

                    <div className="input">
                              <img src={password_icon} alt="Password Icon" />
                              <MypassField label="Confirm password" name="password2" control={control} />
                    </div>
                    
                </div>
                <div className="submit-container">
                    <MyButton type="Reset password" label="Request Password Reset" />
                </div>
            </form>
        </div>
    );
};

export default PasswordReset;