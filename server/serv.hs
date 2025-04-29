-- Echo server program
module Main (main) where

import Control.Concurrent (forkFinally)
import Control.Exception qualified as E
import Control.Monad (forever, unless, void)
import Data.ByteString qualified as S
import Data.List.NonEmpty qualified as NE
import Data.Text as T
import Data.Text.Encoding as T
import Network.Socket
import Network.Socket.ByteString (recv, sendAll)

main :: IO ()
main = runTCPServer Nothing "3000" talk
  where
    talk s = do
      -- Se aumento el buffer
      msg <- recv s 10240
      unless (S.null msg) $ do
        sendAll s (doP msg)
        talk s

-- from the "network-run" package.
runTCPServer :: Maybe HostName -> ServiceName -> (Socket -> IO a) -> IO a
runTCPServer mhost port server = withSocketsDo $ do
  addr <- resolve
  E.bracket (open addr) close loop
  where
    resolve = do
      let hints =
            defaultHints
              { addrFlags = [AI_PASSIVE],
                addrSocketType = Stream
              }
      NE.head <$> getAddrInfo (Just hints) mhost (Just port)
    open addr = E.bracketOnError (openSocket addr) close $ \sock -> do
      setSocketOption sock ReuseAddr 1
      withFdSocket sock setCloseOnExecIfNeeded
      bind sock $ addrAddress addr
      listen sock 1024
      return sock
    loop sock = forever $
      E.bracketOnError (accept sock) (close . fst) $
        \(conn, _peer) ->
          void $
            -- 'forkFinally' alone is unlikely to fail thus leaking @conn@,
            -- but 'E.bracketOnError' above will be necessary if some
            -- non-atomic setups (e.g. spawning a subprocess to handle
            -- @conn@) before proper cleanup of @conn@ is your case
            forkFinally (server conn) (const $ gracefulClose conn 3000)

doP bst = deCad (doL (aCad (bst)))

doL [] = []
doL lin =
  hazL (Prelude.takeWhile (/= '\n') lin)
    ++ doL (Prelude.tail (Prelude.dropWhile (/= '\n') lin))

hazL l = menu l

menu msg
  | (msg > "0") = show (reinas (read msg))
  | (otherwise) = "No entendi"

rev l = Prelude.foldl (#) [] l
  where
    (#) xs x = x : xs

aCad = T.unpack . T.decodeUtf8

deCad = T.encodeUtf8 . T.pack

reinas n = coloca n []

coloca n sol
  | Prelude.length sol == n = [sol]
  | otherwise = Prelude.concatMap intentar [1 .. n]
  where
    intentar r
      | notElem r sol && noAtaca r sol 1 = coloca n (r : sol)
      | otherwise = []

noAtaca _ [] _ = True
noAtaca r (x : xs) d =
  abs (r - x) /= d && noAtaca r xs (d + 1)
