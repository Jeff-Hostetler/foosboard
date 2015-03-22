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
      first_player = Player.create(nickname: "Single Page App")
      second_player = Player.create(nickname: "Distributed System")

      game = Game.create(
        team_1_score: 0,
        team_2_score: 5,
        in_progress: false,
        team_1_defense_id: first_player.id,
        team_1_offense_id: first_player.id,
        team_2_offense_id: second_player.id,
        team_2_defense_id: second_player.id
      )

      get "/games", query = {}, accept_json

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)
      first_game = response_body[:games].first

      expect(first_game[:id]).to eq game.id
      expect(first_game[:team_1_score]).to eq 0
      expect(first_game[:team_2_score]).to eq 5
      expect(first_game[:in_progress]).to eq false

      expect(first_game[:team_1][:defense][:id]).to eq first_player.id
      expect(first_game[:team_1][:offense][:id]).to eq first_player.id
      expect(first_game[:team_2][:offense][:id]).to eq second_player.id
      expect(first_game[:team_2][:defense][:id]).to eq second_player.id

      expect(first_game[:team_1][:defense][:nickname]).
        to eq "Single Page App"
      expect(first_game[:team_1][:offense][:nickname]).
        to eq "Single Page App"
      expect(first_game[:team_2][:offense][:nickname]).
        to eq "Distributed System"
      expect(first_game[:team_2][:defense][:nickname]).
        to eq "Distributed System"
    end
  end

  describe "POST /games" do
    it "creates a game" do
      first_player = Player.create(nickname: "Single Page App")
      second_player = Player.create(nickname: "Distributed System")

      payload = {
        team_1: {
          defense: {id: first_player.id},
          offense: {id: first_player.id}
        },
        team_2: {
          defense: {id: second_player.id},
          offense: {id: second_player.id}
        }
      }.to_json

      post "/games", payload, json_headers

      expect(response.status).to eq 201

      response_body = JSON.parse(response.body, symbolize_names: true)
      created_game = response_body[:game]

      expect(created_game[:id]).to be_present
      expect(created_game[:team_1_score]).to eq 0
      expect(created_game[:team_2_score]).to eq 0
      expect(created_game[:in_progress]).to eq true

      expect(created_game[:team_1][:defense][:id]).to eq first_player.id
      expect(created_game[:team_1][:offense][:id]).to eq first_player.id
      expect(created_game[:team_2][:offense][:id]).to eq second_player.id
      expect(created_game[:team_2][:defense][:id]).to eq second_player.id

      expect(created_game[:team_1][:defense][:nickname]).
        to eq "Single Page App"
      expect(created_game[:team_1][:offense][:nickname]).
        to eq "Single Page App"
      expect(created_game[:team_2][:offense][:nickname]).
        to eq "Distributed System"
      expect(created_game[:team_2][:defense][:nickname]).
        to eq "Distributed System"
    end
  end

  describe "PATCH /games/:id" do
    it "finalizes a game's score" do
      first_player = Player.create(nickname: "Single Page App")
      second_player = Player.create(nickname: "Distributed System")

      game = Game.create(
        team_1_score: 0,
        team_2_score: 0,
        in_progress: true,
        team_1_defense_id: first_player.id,
        team_1_offense_id: first_player.id,
        team_2_offense_id: second_player.id,
        team_2_defense_id: second_player.id
      )

      payload = {
        team_1_score: 5,
        team_2_score: 0
      }.to_json

      patch "/games/#{game.id}", payload, json_headers

      expect(response.status).to eq 200

      response_body = JSON.parse(response.body, symbolize_names: true)
      updated_game = response_body[:game]

      expect(updated_game[:team_1_score]).to eq 5
      expect(updated_game[:team_2_score]).to eq 0
      expect(updated_game[:in_progress]).to eq false
    end
  end
end
