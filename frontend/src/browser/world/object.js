import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import GetGen from "../../utils/getgen";
import loadObjectClient from "../../utils/loadfromclient/loadobjectclient";

function Object({ object }) {
  const [response, setResponse] = useState([]);

  useEffect(() => {
    loadObjectClient(object, setResponse);
  }, [object]);

  if (!response || response.length === 0) {
    return (
      <div className="Object">
        <h3>Loading...</h3>
      </div>
    );
  } else if (response.message) {
    return (
      <div className="Object">
        <h3>{response.message}</h3>
      </div>
    );
  } else {
    return (
      <div className="Object" style={{ whiteSpace: "pre-line" }}>
        {response.generation}
      </div>
    );
  }
}

export default Object;
