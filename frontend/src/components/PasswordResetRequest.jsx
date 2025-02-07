// import React, { useEffect, useState } from 'react'; // Consolidated React import
// import { Link } from 'react-router-dom';
// import '../Login.css';
// import email_icon from '../assets/email.png';
// import MytextField from './forms/MytextField';
// import MyButton from './forms/MyButton';
// import { useForm } from 'react-hook-form';
// import AxiosInstance from './Axiosinstance';
// import { useNavigate } from 'react-router-dom';
// import MyMessage from './Message';

// const PasswordResetRequest = () => {
//     const navigate = useNavigate();
//     const { handleSubmit, control } = useForm();
//     const [showMessage, setShowMessage] = useState(false); // Fixed `useState`

//     const submission = (data) => {
//         AxiosInstance.post(`api/password_reset/`, {
//             username: data.username,
//             email: data.email,
//         })
//         .then((response) => {
//             setShowMessage(true);
//         })
//         .catch((error) => {
//             console.error('Error during password reset request', error);
//         });
//     };

//     return (
//         <div className="container">
//              {showMessage && (
//                     <MyMessage text="If your email exists, you have received an email with instructions for resetting your password." />
//                 )}
//             <form onSubmit={handleSubmit(submission)}>
               
//                 <div className="header">
//                     <div className="text">Request Password Reset</div>
//                 </div>
//                 <div className="inputs">
//                     <div className="input">
//                         <img src={email_icon} alt="Email Icon" />
//                         <MytextField label="Email" name="email" control={control} />
//                     </div>
//                 </div>
//                 <div className="submit-container">
//                     <MyButton type="submit" label="Request Password Reset" />
//                 </div>
//             </form>
//         </div>
//     );
// };

// export default PasswordResetRequest;