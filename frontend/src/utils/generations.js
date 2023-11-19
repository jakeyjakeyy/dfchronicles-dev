import RefreshToken from "./refreshtoken";

async function Generations(request, id, feedback) {
  if (request === "get") {
    return fetch("http://localhost:8000/api/generations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ request: "get", page: id }),
    })
      .then((res) => res.json())
      .then((data) => {
        return data;
      })
      .catch((err) => {
        console.log(err);
        throw err;
      });
  }
  if (request === "Query") {
    return apiCall(request, {
      request: "query",
      generation: id,
    });
  } else if (request === "favorite") {
    return apiCall(request, { request: "favorite", generation: id });
  } else if (request === "comment") {
    return apiCall(request, {
      request: "comment",
      generation: id,
      comment: feedback,
    });
  } else if (request === "deleteComment") {
    return apiCall(request, {
      request: "comment",
      delete: true,
      comment: id,
    });
  } else if (request === "rate") {
    return apiCall(request, {
      request: "rate",
      generation: id,
      rating: feedback,
    });
  }
}

function apiCall(request, data) {
  const token = localStorage.getItem("token");
  return fetch("http://localhost:8000/api/generations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then(async (res) => {
      return HandleRefresh(res, request, data.generation);
    })
    .catch((err) => {
      console.log(err);
      throw err;
    });
}

async function HandleRefresh(data, request, id, feedback) {
  if (data.message === "Invalid token" || data.code === "token_not_valid") {
    const res = await RefreshToken();
    if (res && res.message === "Expired token") {
      return { message: "Please log in again." };
    }
    return Generations(request, id);
  } else {
    return data;
  }
}

export default Generations;
