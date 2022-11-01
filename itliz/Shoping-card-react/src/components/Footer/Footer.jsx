import React from "react";
import { Link } from "react-router-dom";
import "./Footer.css";
import { FaArrowUp } from "react-icons/fa";

export default function Footer() {
  const handelToTop = () => {
    window.scrollTo(0, 0);
  };
  return (
    <footer className="footer">
      <span onClick={handelToTop} className="go_top">
        <FaArrowUp />
      </span>
      <div className="footer_first">
        {/* <img src="images/memory.png" alt="Memory Game" />
        <div className="footer_btn_title_box">
          <p>1

          </p>
          <a
            target={"_blank"}
            href="https://"
            className="btn_link_to_game"
            rel="noreferrer"
          >
            more from me
          </a>
          <a
            target={"_blank"}
            href="https://github.com"
            className="btn_link_to_game"
            rel="noreferrer"
          >
              Source code
          </a>
        </div>
      </div>
      <div className="footer_last">
        <span>Quick access</span>
        <div className="footer_link_box">
          <Link to={"/basket"}>shopping cart</Link>
          <Link to={"/favorite"}>Favorites</Link>
          <a
            target={"_blank"}
            href="https://github.com"
            rel="noreferrer"
          >
            View the source code of the project on GitHub
          </a>
        </div> */}
      </div>
    </footer>
  );
}
