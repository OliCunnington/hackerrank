{-# LANGUAGE FlexibleInstances, UndecidableInstances, DuplicateRecordFields #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.List
import Data.List.Split
import Data.Set
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

expo :: Double -> Double -> Double
expo x n |n <= 1 = x + 1
         |otherwise = ((x**n)/(product[1..n])) + (expo x (n-1))

main :: IO()
main = do
    n <- readLn :: IO Int

    forM_ [1..n] $ \n_itr -> do
        x <- readLn :: IO Double
        print (expo x 9)
    
                
    
