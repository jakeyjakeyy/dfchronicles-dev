import React from "react";
import "./listitem.css";

function ListItem({ name, name2, id, onClick }) {
  return (
    <div className="ListItem" id={id} key={id} onClick={onClick}>
      <div className="ListItemName" id={id} onClick={onClick}>
        {name}
      </div>
      <div className="ListItemName2" id={id} onClick={onClick}>
        {name2}
      </div>
    </div>
  );
}

export default ListItem;
