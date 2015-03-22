require "rails_helper"

RSpec.describe "Players API" do
  let(:accept_json) do
    {"Accept" => "application/json" }
  end

  describe "GET /players" do
    it "returns all the players" do
      player = Player.create(nickname: "Person McSplashyPants")

      get "/players", accept_json

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body.first[:id]).to eq player.id
      expect(response_body.first[:nickname]).to eq "Person McSplashyPants"
    end
  end
end
