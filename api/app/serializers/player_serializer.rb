class PlayerSerializer < ActiveModel::Serializer
  attributes(:id,
             :nickname)
end
