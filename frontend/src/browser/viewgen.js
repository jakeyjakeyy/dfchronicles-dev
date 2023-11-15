import React from "react";

function ViewGen({ gen }) {
  console.log(gen);
  return (
    <div className="ViewGen">
      <h1>ViewGen</h1>
      <div style={{ whiteSpace: "pre-wrap" }}>{gen.generation}</div>
    </div>
  );
}

export default ViewGen;
