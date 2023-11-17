import React from "react";
import { useState, useEffect } from "react";
import "./userpage.css";
import GetUser from "../../utils/getuser";
import Card from "./card";

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
            <div className="TopRow">
              <div className="Favorites">
                <Card
                  title="Favorites"
                  number={userdata.user_favorites.length}
                />
              </div>
              <div className="Comments">
                <Card title="Comments" number={userdata.user_comments.length} />
              </div>
            </div>
            <div className="Generations">
              <Card title="Generations" number={userdata.generations.length} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default UserPage;
