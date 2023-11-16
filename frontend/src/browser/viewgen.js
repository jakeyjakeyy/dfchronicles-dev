import React from "react";
import "./viewgen.css";
import { FaRegStar, FaStar, FaHeart, FaRegHeart } from "react-icons/fa";
import { useState, useEffect } from "react";
import Generations from "../utils/generations";

function ViewGen({ gen }) {
  const [isLoading, setIsLoading] = useState(true);
  const [favorite, setFavorite] = React.useState(false);
  const [comments, setComments] = React.useState([]);
  const [comment, setComment] = React.useState("");

  useEffect(() => {
    // API call to check if favorite
    async function fetchData() {
      const data = await Generations("favoriteQuery", gen.id);
      if (data.message === "Favorite") {
        setFavorite(true);
      } else {
        setFavorite(false);
      }
    }
    // Get comments
    async function fetchComments() {
      Generations("commentQuery", gen.id).then((data) => {
        console.log(data);
        if (data.comments) {
          setComments(data.comments);
          setIsLoading(false);
        } else {
          console.log(data);
          setIsLoading(false);
        }
      });
    }
    fetchData();
    fetchComments();
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
          Generations("commentQuery", gen.id).then((data) => {
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

  return (
    <div className="ViewGen">
      <div className="ViewGenHeader">
        <h3>{gen.title}</h3>
        <h4>{gen.user}</h4>
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
      <div className="ViewGenContent" style={{ whiteSpace: "pre-wrap" }}>
        <p>{gen.generation}</p>
      </div>
      <div className="CommentsDiv">
        <h4>Comments</h4>
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
        <div className="Comments">
          {isLoading ? (
            <p>Loading comments...</p>
          ) : comments.length === 0 ? (
            <p>No comments yet</p>
          ) : (
            comments.map((comment) => (
              <div className="ViewGenComment" key={comment.id}>
                <div className="ViewGenCommentHeader">
                  <h5>{comment.user}</h5>
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
