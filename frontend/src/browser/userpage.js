import React from "react";
import { useState, useEffect } from "react";
import "./userpage.css";
import GetUser from "../utils/getuser";

function UserPage() {
  const username = localStorage.getItem("username");
  const [userdata, setUserdata] = useState(null);
  useEffect(() => {
    GetUser().then((result) => {
      setUserdata(result);
    });
  }, []);

  if (userdata === null) {
    return (
      <div className="UserPage">
        <div className="Header">
          <h2>{username}</h2>
        </div>
        <div className="Body">
          <p>Loading...</p>
        </div>
      </div>
    );
  } else {
    console.log(userdata);
    return (
      <div className="UserPage">
        <div className="Header">
          <h2>{username}</h2>
        </div>
        <div className="Body">
          <div className="Selections">
            <div className="Favorites"></div>
            <div className="Generations"></div>
            <div className="Comments"></div>
          </div>
        </div>
      </div>
    );
  }
}

export default UserPage;
