import RefreshToken from "./refreshtoken";

async function GetUser(id, request) {
  if (id === "Favorites") {
    return ApiCall(id, { fetch: "favorites", favorites: request });
  } else if (id === "Comments") {
    return ApiCall(id, { fetch: "comments", comments: request });
  }

  const token = localStorage.getItem("token");
  return fetch(`http://localhost:8000/api/user`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
  })
    .then((res) => res.json())
    .then(async (data) => {
      if (data.message === "Invalid token" || data.code === "token_not_valid") {
        const res = await RefreshToken();
        if (res && res.message === "Expired token") {
          return { message: "Please log in again." };
        }
        return GetUser(id);
      } else {
        return data;
      }
    })
    .catch((err) => {
      console.log(err);
      throw err;
    });
}

function ApiCall(id, data) {
  const token = localStorage.getItem("token");
  return fetch(`http://localhost:8000/api/user`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then(async (data) => {
      if (data.message === "Invalid token" || data.code === "token_not_valid") {
        const res = await RefreshToken();
        if (res && res.message === "Expired token") {
          return { message: "Please log in again." };
        }
        return GetUser(id);
      } else {
        return data;
      }
    })
    .catch((err) => {
      console.log(err);
      throw err;
    });
}

export default GetUser;
