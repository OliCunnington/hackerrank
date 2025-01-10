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

loop :: Int -> (IO()) -> IO()
loop 0 _ = return ()
loop n f =
 do
  f
  loop (n - 1) f

main :: IO()
main = do
    n <- readLn :: IO Int
    loop n (do putStrLn "Hello World")
    -- Print "Hello World" on a new line 'n' times.
    
