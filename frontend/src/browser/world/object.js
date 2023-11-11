import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import GetGen from "../../utils/getgen";
import loadObjectClient from "../../utils/loadfromclient/loadobjectclient";

function Object({ object, legendsxml, legendsplusxml }) {
  const [response, setResponse] = useState([]);
  const [data, setData] = useState([]);
  console.log(legendsxml, legendsplusxml);

  useEffect(() => {
    setData(loadObjectClient(object, setResponse, legendsxml, legendsplusxml));
  }, [object]);
  useEffect(() => {
    async function fetchData() {
      if (data.length === 0) {
        return;
      }
      console.log(data);
      const loadeddata = await GetGen(data);
      setResponse(loadeddata);
    }
    fetchData();
  }, [data]);

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
      <div className="Object" style={{ whiteSpace: "pre-wrap" }}>
        {response.generation}
      </div>
    );
  }
}

export default Object;
