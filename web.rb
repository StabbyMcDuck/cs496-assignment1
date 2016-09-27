require 'sinatra'

get '/' do
  "The current date and time: " Time.now.strftime("%d/%m/%Y %H:%M")
end
