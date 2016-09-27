require 'sinatra'

get '/' do
  Time.now.strftime("%d/%m/%Y %H:%M")
end
