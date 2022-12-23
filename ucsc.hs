--import libraries
import Data.List
import Data.Char
import Data.Maybe
import Data.Order

-- Create a function to test the union-closed conjecture
--
-- The conjecture is that if a set is union-closed, then the union of any two
-- elements of the set is also in the set.

-- The function should take a set and a function that tests whether a pair of
-- elements is in the set. It should return True if the conjecture holds for
-- the set and the function, and False otherwise.
-- The function should be called unionClosed.

unionClosed :: (a -> a -> Bool) -> [a] -> Bool
unionClosed f xs = and [f x y | x <- xs, y <- xs, not (f x y)]


