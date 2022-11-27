import React, { createContext, useReducer } from "react";
import allProducts from "../../Data"; 
import axios from 'axios';

const ProductDB = 'http://127.0.0.1:8000/products/'



const initialFilterState = {
  filteredItems: [...allProducts],
  searchKey: ""
};
const filterItemsHandler = (key) => {
  const filteredItems = allProducts.filter((product) => {
    return product.category === key;
  });

  return { filteredItems };
};

const filterReduce = (state, action) => {
  switch (action.type) {
    case "SEARCH_KEYWORD":
      state.searchKey = action.payload;
      return {
        ...state
      };
    case "ALL":
      state.filteredItems = [...allProducts];
      return {
        ...state
      };
    case "VEGETABLE":
      return {
        ...filterItemsHandler("veg")
      };
    case "FRUIT":
      return {
        ...filterItemsHandler("fruit")
      };
    case "NUTS":
      return {
        ...filterItemsHandler("nuts")
      };
    case "BEANS":
      return {
        ...filterItemsHandler("beans")
      };
    default:
      return state;
  }
};

export const FilterContext = createContext();
export const FilterDispath = createContext();

export default function ContextFilter({ children }) {
  const [state, dispath] = useReducer(filterReduce, initialFilterState);
  return (
    <FilterContext.Provider value={{ state }}>
      <FilterDispath.Provider value={{ dispath }}>
        {children}
      </FilterDispath.Provider>
    </FilterContext.Provider>
  );
}
