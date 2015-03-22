require "rails_helper"

RSpec.describe "Games API" do
  let(:accept_json) do
    {"Accept" => "application/json" }
  end

  let(:json_content_type) do
    {"Content-Type" => "application/json"}
  end

  let(:json_headers) do
    accept_json.merge(json_content_type)
  end

  describe "GET /games" do
    it "returns all the games" do
      game = Game.create(
        team_1_score: 0,
        team_2_score: 5,
        in_progress: false,
        team_1_defense_id: 123,
        team_1_offense_id: 123,
        team_2_offense_id: 987,
        team_2_defense_id: 987
      )

      get "/games", query = {}, accept_json

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body.first[:id]).to eq game.id
      expect(response_body.first[:team_1_score]).to eq 0
      expect(response_body.first[:team_2_score]).to eq 5
      expect(response_body.first[:in_progress]).to eq false
      expect(response_body.first[:team_1_defense_id]).to eq 123
      expect(response_body.first[:team_1_offense_id]).to eq 123
      expect(response_body.first[:team_2_offense_id]).to eq 987
      expect(response_body.first[:team_2_defense_id]).to eq 987
    end
  end

  describe "POST /games" do
    it "creates a game" do
      first_player = Player.create(nickname: "Single Page App")
      second_player = Player.create(nickname: "Distributed System")

      payload = {
        team_1_defense_id: first_player.id,
        team_1_offense_id: first_player.id,
        team_2_offense_id: second_player.id,
        team_2_defense_id: second_player.id,
      }.to_json

      post "/games", payload, json_headers

      expect(response.status).to eq 201

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body[:team_1_score]).to eq 0
      expect(response_body[:team_2_score]).to eq 0
      expect(response_body[:team_1_defense_id]).to eq first_player.id
      expect(response_body[:team_1_offense_id]).to eq first_player.id
      expect(response_body[:team_2_offense_id]).to eq second_player.id
      expect(response_body[:team_2_defense_id]).to eq second_player.id
      expect(response_body[:in_progress]).to eq true
    end
  end

  describe "PATCH /games/:id" do
    it "finalizes a game's score" do
      game = Game.create(
        team_1_score: 0,
        team_2_score: 0,
        in_progress: true,
        team_1_defense_id: 123,
        team_1_offense_id: 123,
        team_2_offense_id: 987,
        team_2_defense_id: 987
      )

      payload = {
        team_1_score: 5,
        team_2_score: 0
      }.to_json

      patch "/games/#{game.id}", payload, json_headers

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)

      expect(response_body[:team_1_score]).to eq 5
      expect(response_body[:team_2_score]).to eq 0
      expect(response_body[:in_progress]).to eq false
    end
  end
end
