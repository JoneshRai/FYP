// import React from "react";
// import AxiosInstance from "./Axiosinstance";
// import { useNavigate } from "react-router-dom";
// import "./Home.css"; // Assuming you have a CSS file for styles
// import { FaHome, FaComments, FaPlus, FaSignOutAlt, FaUser } from "react-icons/fa";
// import { ListItem, ListItemButton } from "@mui/material";

// const Home = () => {
//   console.log("home ")
//   const navigate = useNavigate()
//   const logoutUser = () =>{
//     AxiosInstance.post(`logoutall/,{}`)
//     .then (() => {
//       localStorage.removeItem("Token")
//       navigate('/')
//     })
//   }
//   return (
//     <div className="app-container">
//       {/* Sidebar */}
//           <div className="sidebar">
//       <button className="icon-button">
//         <FaHome className="icon" />
//       </button>
//       <button className="icon-button">
//         <FaComments className="icon" />
//       </button>
//       <button className="icon-button">
//         <FaPlus className="icon" />
//       </button>
//       <ListItemButton onClick={logoutUser} className="icon-button">
//         <FaSignOutAlt className="icon" />
//       </ListItemButton>
//     </div>


//       {/* Main content */}
//       <div className="main-content">
//         {/* Top Bar */}
//         <div className="top-bar">
//           <input
//             type="text"
//             className="search-bar"
//             placeholder="Search"
//           />
//           <button className="icon-button">
//             <FaUser className="account-icon" />
//           </button>
//         </div>

//          {/* Cards Section */}
//         <div className="cards-container">
//           <div className="card">
//             <img src="../assets/Background.jpeg" className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 1</h5>
//               <p className="card-text">
//                 Some quick example text to build on the card title and make up the bulk of the card's content.
//               </p>
//               <a href="" className="btn btn-primary">View</a>
//             </div>
//           </div>

//           <div className="card">
//             <img src="..." className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 2</h5>
//               <p className="card-text">
//                 Some quick example text to build on the card title and make up the bulk of the card's content.
//               </p>
//               <a href="#" className="btn btn-primary">View</a>
//             </div>
//           </div>

//           <div className="card">
//             <img src="..." className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 3</h5>
//               <p className="card-text">
//                 Some quick example text to build on the card title and make up the bulk of the card's content.
//               </p>
//               <a href="#" className="btn btn-primary">View</a>
//             </div>
//           </div>

//           {/* New Card */}
//           <div className="card">
//             <img src="..." className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 4</h5>
//               <p className="card-text">
//                 Another quick example text to add to the card's content.
//               </p>
//               <a href="#" className="btn btn-primary">View</a>
//             </div>
//           </div>


//           <div className="card">
//             <img src="..." className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 4</h5>
//               <p className="card-text">
//                 Another quick example text to add to the card's content.
//               </p>
//               <a href="#" className="btn btn-primary">View</a>
//             </div>
//           </div>

//           <div className="card">
//             <img src="../assets/Background.jpeg'" className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 4</h5>
//               <p className="card-text">
//                 Another quick example text to add to the card's content.
//               </p>
//               <a href="#" className="btn btn-primary">View</a>
//             </div>
//           </div>

          
//           <div className="card">
//             <img src="../assets/Background.jpeg'" className="card-img-top" alt="..." />
//             <div className="card-body">
//               <h5 className="card-title">Card title 4</h5>
//               <p className="card-text">
//                 Another quick example text to add to the card's content.
//               </p>
//               <a href="#" className="btn btn-primary">View</a>
//             </div>
//           </div>


//           </div>
//       </div>
//     </div>
//   );
// };

// export default Home;
