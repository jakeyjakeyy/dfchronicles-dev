import React from "react";
import { useState, useEffect } from "react";
import "./userpage.css";
import GetUser from "../../utils/getuser";
import Card from "./card";
import ListItem from "../listitem";
import ViewGen from "../viewgen";

function UserPage({ onAppSelect, onAppSelectId }) {
  const username = localStorage.getItem("username");
  const [userdata, setUserdata] = useState(null);
  const [generations, setGenerations] = useState(null);
  const [gendata, setGendata] = useState(null);

  useEffect(() => {
    GetUser().then((result) => {
      setUserdata(result);
    });
  }, []);

  async function HandleClick(name) {
    if (name === "Favorites") {
      let favorites = userdata.user_favorites;
      let result = await GetUser("Favorites", favorites);
      console.log(result);
      setGenerations(result);
    } else if (name === "Comments") {
      let comments = userdata.user_comments;
      let result = await GetUser("Comments", comments);
      console.log(result);
      setGenerations(result);
    } else if (name === "Generations") {
      let generations = userdata.generations;
      let result = await GetUser("Generations", generations);
      console.log(result);
      setGenerations(result);
    }
  }

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
  } else if (gendata !== null) {
    console.log(gendata);
    onAppSelect("ViewGen");
    onAppSelectId(gendata);
  } else if (userdata && generations === null) {
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
                  onClick={() => HandleClick("Favorites")}
                />
              </div>
              <div className="Comments">
                <Card
                  title="Comments"
                  number={userdata.user_comments.length}
                  onClick={() => {
                    HandleClick("Comments");
                  }}
                />
              </div>
            </div>
            <div className="Generation">
              <Card
                title="Generations"
                number={userdata.generations.length}
                onClick={() => {
                  HandleClick("Generations");
                }}
              />
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    console.log(generations);
    return (
      <div className="UserPage">
        <div className="Header">
          <h2>{username}</h2>
        </div>
        <div className="Body">
          <div className="Generations">
            {generations.generations.map((gen) => (
              <ListItem
                key={gen.id}
                id={gen.id}
                name={gen.title}
                name2={gen.generation}
                ratings={gen.ratings}
                favorites={gen.favorites}
                comments={gen.comments}
                username={gen.user}
                onClick={() => {
                  setGendata(gen);
                }}
              />
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default UserPage;
