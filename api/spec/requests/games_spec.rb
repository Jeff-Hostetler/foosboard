require "rails_helper"

RSpec.describe "Games API" do
  let(:accept_json) do
    {"Accept" => "application/json" }
  end

  describe "GET /games" do
    it "returns all the games" do
      game = Game.create(team_1_score: 0, team_2_score: 5, in_progress: false)

      get "/games", accept_json

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body.first[:id]).to eq game.id
      expect(response_body.first[:team_1_score]).to eq 0
      expect(response_body.first[:team_2_score]).to eq 5
      expect(response_body.first[:in_progress]).to eq false
    end
  end
end
