# typed: true

# DO NOT EDIT MANUALLY
# This is an autogenerated file for types exported from the `json_schemer` gem.
# Please instead update this file by running `bin/tapioca gem json_schemer`.

module JSONSchemer
  class << self
    def schema(schema, **options); end

    private

    def draft_class(schema); end
  end
end

class JSONSchemer::CachedRefResolver < ::JSONSchemer::CachedResolver; end

class JSONSchemer::CachedResolver
  def initialize(&resolver); end

  def call(*args); end
end

JSONSchemer::DEFAULT_META_SCHEMA = T.let(T.unsafe(nil), String)
JSONSchemer::DRAFT_CLASS_BY_META_SCHEMA = T.let(T.unsafe(nil), Hash)

module JSONSchemer::Errors
  class << self
    def pretty(error); end
  end
end

JSONSchemer::FILE_URI_REF_RESOLVER = T.let(T.unsafe(nil), Proc)

module JSONSchemer::Format
  def iri_escape(data); end
  def parse_uri_scheme(data); end
  def valid_date_time?(data); end
  def valid_email?(data); end
  def valid_hostname?(data); end
  def valid_ip?(data, type); end
  def valid_json?(data); end
  def valid_json_pointer?(data); end
  def valid_relative_json_pointer?(data); end
  def valid_spec_format?(data, format); end
  def valid_uri?(data); end
  def valid_uri_reference?(data); end
  def valid_uri_template?(data); end
end

JSONSchemer::Format::DATE_TIME_OFFSET_REGEX = T.let(T.unsafe(nil), Regexp)
JSONSchemer::Format::EMAIL_REGEX = T.let(T.unsafe(nil), Regexp)
JSONSchemer::Format::HOSTNAME_REGEX = T.let(T.unsafe(nil), Regexp)
JSONSchemer::Format::INVALID_QUERY_REGEX = T.let(T.unsafe(nil), Regexp)
JSONSchemer::Format::JSON_POINTER_REGEX = T.let(T.unsafe(nil), Regexp)
JSONSchemer::Format::JSON_POINTER_REGEX_STRING = T.let(T.unsafe(nil), String)
JSONSchemer::Format::LABEL_REGEX_STRING = T.let(T.unsafe(nil), String)
JSONSchemer::Format::RELATIVE_JSON_POINTER_REGEX = T.let(T.unsafe(nil), Regexp)
class JSONSchemer::InvalidFileURI < ::StandardError; end
class JSONSchemer::InvalidRefResolution < ::StandardError; end
class JSONSchemer::InvalidRegexpResolution < ::StandardError; end
class JSONSchemer::InvalidSymbolKey < ::StandardError; end
module JSONSchemer::Schema; end

class JSONSchemer::Schema::Base
  include ::JSONSchemer::Format

  def initialize(schema, format: T.unsafe(nil), insert_property_defaults: T.unsafe(nil), before_property_validation: T.unsafe(nil), after_property_validation: T.unsafe(nil), formats: T.unsafe(nil), keywords: T.unsafe(nil), ref_resolver: T.unsafe(nil), regexp_resolver: T.unsafe(nil)); end

  def valid?(data); end
  def validate(data); end

  protected

  def ids; end
  def valid_instance?(instance); end
  def validate_instance(instance, &block); end

  private

  def child(schema); end
  def custom_format?(format); end
  def error(instance, type, details = T.unsafe(nil)); end
  def format?; end
  def formats; end
  def id_keyword; end
  def join_uri(a, b); end
  def keywords; end
  def pointer_uri(schema, pointer); end
  def ref_resolver; end
  def regexp_resolver; end
  def resolve_ids(schema, ids = T.unsafe(nil), parent_uri = T.unsafe(nil), pointer = T.unsafe(nil)); end
  def resolve_ref(uri); end
  def resolve_regexp(pattern); end
  def root; end
  def safe_strict_decode64(data); end
  def spec_format?(format); end
  def validate_array(instance, &block); end
  def validate_class(instance, &block); end
  def validate_custom_format(instance, custom_format); end
  def validate_exclusive_maximum(instance, exclusive_maximum, maximum); end
  def validate_exclusive_minimum(instance, exclusive_minimum, minimum); end
  def validate_integer(instance, &block); end
  def validate_number(instance, &block); end
  def validate_numeric(instance, &block); end
  def validate_object(instance, &block); end
  def validate_ref(instance, ref, &block); end
  def validate_string(instance, &block); end
  def validate_type(instance, type, &block); end
end

JSONSchemer::Schema::Base::BOOLEANS = T.let(T.unsafe(nil), Set)
JSONSchemer::Schema::Base::DEFAULT_REF_RESOLVER = T.let(T.unsafe(nil), Proc)
JSONSchemer::Schema::Base::ECMA_262_REGEXP_RESOLVER = T.let(T.unsafe(nil), Proc)
JSONSchemer::Schema::Base::ID_KEYWORD = T.let(T.unsafe(nil), String)
JSONSchemer::Schema::Base::INSERT_DEFAULT_PROPERTY = T.let(T.unsafe(nil), Proc)

class JSONSchemer::Schema::Base::Instance < ::Struct
  def after_property_validation; end
  def after_property_validation=(_); end
  def before_property_validation; end
  def before_property_validation=(_); end
  def data; end
  def data=(_); end
  def data_pointer; end
  def data_pointer=(_); end
  def merge(data: T.unsafe(nil), data_pointer: T.unsafe(nil), schema: T.unsafe(nil), schema_pointer: T.unsafe(nil), parent_uri: T.unsafe(nil), before_property_validation: T.unsafe(nil), after_property_validation: T.unsafe(nil)); end
  def parent_uri; end
  def parent_uri=(_); end
  def schema; end
  def schema=(_); end
  def schema_pointer; end
  def schema_pointer=(_); end

  class << self
    def [](*_arg0); end
    def inspect; end
    def members; end
    def new(*_arg0); end
  end
end

JSONSchemer::Schema::Base::NET_HTTP_REF_RESOLVER = T.let(T.unsafe(nil), Proc)
JSONSchemer::Schema::Base::RUBY_REGEX_ANCHORS_TO_ECMA_262 = T.let(T.unsafe(nil), Hash)

class JSONSchemer::Schema::Draft4 < ::JSONSchemer::Schema::Base
  private

  def id_keyword; end
  def supported_format?(format); end
  def validate_exclusive_maximum(instance, exclusive_maximum, maximum); end
  def validate_exclusive_minimum(instance, exclusive_minimum, minimum); end
  def validate_integer(instance, &block); end
end

JSONSchemer::Schema::Draft4::ID_KEYWORD = T.let(T.unsafe(nil), String)
JSONSchemer::Schema::Draft4::SUPPORTED_FORMATS = T.let(T.unsafe(nil), Set)

class JSONSchemer::Schema::Draft6 < ::JSONSchemer::Schema::Base
  private

  def supported_format?(format); end
end

JSONSchemer::Schema::Draft6::SUPPORTED_FORMATS = T.let(T.unsafe(nil), Set)

class JSONSchemer::Schema::Draft7 < ::JSONSchemer::Schema::Base
  private

  def supported_format?(format); end
end

JSONSchemer::Schema::Draft7::SUPPORTED_FORMATS = T.let(T.unsafe(nil), Set)
class JSONSchemer::UnknownRef < ::StandardError; end
class JSONSchemer::UnsupportedMetaSchema < ::StandardError; end
JSONSchemer::VERSION = T.let(T.unsafe(nil), String)
JSONSchemer::WINDOWS_URI_PATH_REGEX = T.let(T.unsafe(nil), Regexp)
