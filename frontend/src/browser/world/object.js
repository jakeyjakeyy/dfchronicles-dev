import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import GetGen from "../../utils/getgen";

function Object({ object }) {
  const [response, setResponse] = useState([]);

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
