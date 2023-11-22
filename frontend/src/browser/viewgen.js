import React from "react";
import "./viewgen.css";
import { FaHeart, FaRegHeart } from "react-icons/fa";
import { FaRegTrashCan } from "react-icons/fa6";
import { useState, useEffect } from "react";
import Generations from "../utils/generations";
import Rating from "./rating";

function ViewGen({ gen }) {
  const [isLoading, setIsLoading] = useState(true);
  const [favorite, setFavorite] = React.useState(false);
  const [comments, setComments] = React.useState([]);
  const [comment, setComment] = React.useState("");
  const [rating, setRating] = React.useState(0);

  useEffect(() => {
    // API call to fetch generation data
    async function fetchData() {
      if (!localStorage.getItem("username")) {
        const data = await Generations("GET", gen.id);
        if (data.comments) {
          setComments(data.comments);
          setIsLoading(false);
        }
      } else {
        const data = await Generations("Query", gen.id);
        if (data.userfavorite) {
          setFavorite(true);
        } else {
          setFavorite(false);
        }
        if (data.comments) {
          setComments(data.comments);
          setIsLoading(false);
        } else {
          setIsLoading(false);
        }
        if (data.userrating) {
          console.log(data.userrating);
          setRating(data.userrating);
        }
      }
    }
    fetchData();
  }, []);
  const handleFavoriteClick = () => {
    // API call to set favorite
    async function fetchData() {
      await Generations("favorite", gen.id).then((data) => {
        if (
          data.message === "Favorite added" ||
          data.message === "Favorite removed"
        ) {
          setFavorite(!favorite);
        } else {
          console.log(data);
        }
      });
    }
    fetchData();
  };
  const submitComment = (e) => {
    e.preventDefault();
    // API call to submit comment
    async function fetchData() {
      await Generations("comment", gen.id, comment).then((data) => {
        if (data.message === "Comment added") {
          setComment("");
          Generations("Query", gen.id).then((data) => {
            if (data.comments) {
              setComments(data.comments);
            } else {
              console.log(data);
            }
          });
        } else {
          console.log(data);
        }
      });
    }
    fetchData();
  };
  const handleSetRating = (newRating) => {
    if (rating === newRating) {
      newRating = 0;
    }
    setRating(newRating);
    Generations("rate", gen.id, newRating);
  };

  return (
    <div className="ViewGen">
      <div className="ViewGenHeader">
        <h3>{gen.title}</h3>
        <h4>{gen.user}</h4>
        <div className="Favorite">
          {!favorite && (
            <FaRegHeart
              color={"red"}
              className="FavButton"
              onClick={handleFavoriteClick}
            />
          )}
          {favorite && (
            <FaHeart
              color={"red"}
              className="FavButton"
              onClick={handleFavoriteClick}
            />
          )}
        </div>
        <div className="Rating">
          <Rating rating={rating} onClick={handleSetRating} />
        </div>
      </div>
      <div className="ViewGenContent" style={{ whiteSpace: "pre-wrap" }}>
        <p>{gen.generation}</p>
      </div>
      <div className="CommentsDiv">
        <h4 className="CommentsHeader">Comments</h4>
        <div className="CommentForm">
          <textarea
            className="CommentInput"
            type="text"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            placeholder="Leave a comment..."
          />
          <button
            className="CommentSubmit"
            type="submit"
            onClick={submitComment}
          >
            Submit
          </button>
        </div>
        <div className="GenComments">
          {isLoading ? (
            <p>Loading comments...</p>
          ) : comments.length === 0 ? (
            <p>No comments yet</p>
          ) : (
            comments.map((comment) => (
              <div className="ViewGenComment" key={comment.id}>
                <div className="ViewGenCommentHeader">
                  <h5>{comment.user}</h5>
                  {comment.user === localStorage.getItem("username") && (
                    <div className="DeleteComment">
                      <FaRegTrashCan
                        size={16}
                        onClick={() => {
                          Generations("deleteComment", comment.id).then(
                            (data) => {
                              if (data.message === "Comment removed") {
                                console.log(data);
                                Generations("Query", gen.id).then((data) => {
                                  if (data.comments) {
                                    setComments(data.comments);
                                  } else {
                                    console.log(data);
                                  }
                                });
                              } else {
                                console.log(data);
                              }
                            }
                          );
                        }}
                      />
                    </div>
                  )}
                </div>
                <div className="ViewGenCommentContent">
                  <p>{comment.comment}</p>
                </div>
                <div className="ViewGenCommentFooter">
                  <small>{new Date(comment.time).toLocaleString()}</small>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default ViewGen;
